// classes
class Checkpoint {
  x: number;
  y: number;
  diam: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
    this.diam = 600;
  }
}

class Pod {
  x: number;
  y: number;
  prev_x: number;
  prev_y: number;
  direction: [number, number]; // direction vector (x, y)

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }

  updatePositionAndDirection(x: number, y: number) {
    this.prev_x = this.x;
    this.prev_y = this.y;

    this.x = x;
    this.y = y;

    let dirX: number = this.x - this.prev_x;
    let dirY: number = this.y - this.prev_y;
    this.direction = [dirX, dirY];
  }
}

class opponentPod extends Pod {}

class ownedPod extends Pod {
  power: number | "BOOST";
  boost: boolean;
  destinationX: number;
  destinationY: number;
  destinationDist: number;
  angleBtwPodAndDestination: number;
  angleBtwPodDirectionAndDestination: number;
  distOppPod: number;

  constructor(x: number, y: number, boost: boolean) {
    super(x, y);
    this.boost = boost;
  }

  updatePositionAndDirection(x: number, y: number) {
    this.prev_x = this.x;
    this.prev_y = this.y;

    this.x = x;
    this.y = y;

    let dirX: number = this.x - this.prev_x;
    let dirY: number = this.y - this.prev_y;
    this.direction = [dirX, dirY];

    this.angleBtwPodDirectionAndDestination =
      this.angleBtwDirectionAndDestination();
  }

  angleBtwDirectionAndDestination(): number {
    // u (xu, yu) the vector direction get from previous position and actual position
    // v (xv, yv) the vector destination get from actual position et destination point
    // alpha = cos-1( (u.v) / (||u||.||v||) )
    let xu: number = this.direction[0];
    let yu: number = this.direction[1];
    let xv: number = this.destinationX - this.x;
    let yv: number = this.destinationY - this.y;
    let scalarProductUV: number = xu * xv + yu * yv;
    let normeU: number = Math.sqrt(xu ** 2 + yu ** 2);
    let normeV: number = Math.sqrt(xv ** 2 + yv ** 2);
    let alphaRadian: number = Math.acos(scalarProductUV / (normeU * normeV));
    let alpha: number = alphaRadian * (180 / Math.PI);
    return Math.round(alpha);
  }

  handleDestination(checkpoint: Checkpoint, dist: number, angle: number): void {
    this.destinationX = checkpoint.x;
    this.destinationY = checkpoint.y;
    this.destinationDist = dist;
    this.angleBtwPodAndDestination = angle;
  }

  handlePower(pod: Pod): void {
    this.distOppPod = this.distBtwPods(pod);

    // driving parameters
    let isCollisionRisk: boolean = this.distOppPod < 800;
    let isShortDistToCheckPoint: boolean =
      150 < this.destinationDist && this.destinationDist < 750;
    let isMediumDistToCheckPoint: boolean =
      750 < this.destinationDist && this.destinationDist < 1250;
    let isOptimalAngle: boolean =
      Math.abs(this.angleBtwPodAndDestination) < 100;
    let isStopTurnAroundTime: boolean =
      this.destinationDist < 2000 &&
      this.angleBtwPodDirectionAndDestination > 40;

    switch (true) {
      case isStopTurnAroundTime:
        this.power = 70;
        break;
      case !isOptimalAngle:
        this.power = 30;
        break;
      case isMediumDistToCheckPoint:
        this.power = 50;
        break;
      case isShortDistToCheckPoint:
        this.power = 0;
        break;
      case isCollisionRisk:
        this.power = 100;
        break;
      default:
        this.power = 100;
        break;
    }
  }

  handleBoost(): void {
    let isLongDistance: boolean = this.destinationDist > 6000;
    let isGoodAngleForBoost: boolean =
      Math.abs(this.angleBtwPodAndDestination) < 20;

    if (this.boost && isLongDistance && isGoodAngleForBoost) {
      this.power = "BOOST";
      this.boost = false;
    }
  }

  distBtwPods(pod: Pod): number {
    let x1: number = this.x;
    let y1: number = this.y;
    let x2: number = pod.x;
    let y2: number = pod.y;
    return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
  }
}

// global variables
let nextCheckpoint = new Checkpoint(0, 0);
let myPod = new ownedPod(0, 0, true);
let oppPod = new opponentPod(0, 0);

// game loop ---------------------------------------------------------------------------------------------------------
while (true) {
  var inputs: string[] = readline().split(" ");
  const x: number = parseInt(inputs[0]);
  const y: number = parseInt(inputs[1]);
  const nextCheckpointX: number = parseInt(inputs[2]); // x position of the next check point
  const nextCheckpointY: number = parseInt(inputs[3]); // y position of the next check point
  const nextCheckpointDist: number = parseInt(inputs[4]); // distance to the next checkpoint
  const nextCheckpointAngle: number = parseInt(inputs[5]); // angle between your pod orientation and the direction of the next checkpoint
  var inputs: string[] = readline().split(" ");
  const opponentX: number = parseInt(inputs[0]);
  const opponentY: number = parseInt(inputs[1]);

  // update data
  nextCheckpoint.x = nextCheckpointX;
  nextCheckpoint.y = nextCheckpointY;
  myPod.updatePositionAndDirection(x, y);
  oppPod.updatePositionAndDirection(opponentX, opponentY);

  // myPod controls
  myPod.handleDestination(
    nextCheckpoint,
    nextCheckpointDist,
    nextCheckpointAngle
  );
  myPod.handlePower(oppPod);
  myPod.handleBoost();

  //log indicators
  console.error("my Pod : ", myPod);
  // console.error("opp Pod : ", oppPod);

  //actions
  let power: number | string = 100;
  console.log(myPod.destinationX, myPod.destinationY, myPod.power);
}
