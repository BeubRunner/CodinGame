// functions declaration  ------------------------------------------------------------------------------------------------

const dijkstraDistPath = (graph, initialNode) => {
    /*
    takes a graph and a initial node & returns an object of 2 dictionnaries :
        dist : {0: int<shortest dist between initial node and 0>, 1:int, ...}
        path : {0: array<shortest path between initial node and 0>, 1:array, ...}
    */

    let currentNode = initialNode;

    let currentDist = {}
    let shortesWayDict = {}
    // Mark the selected initial node with a current distance of 0 and the rest with infinity
    for (let i=0; i<graph.length; i++) {
        currentDist[i] = i === currentNode ? 0 : Infinity;
        shortesWayDict[i] = i === currentNode ? [i] : [];
    }

    let visited = [];
    while (visited.length !== graph.length) {
        let queue = [];
        let nextNode = currentNode;
        let nextNodeDist = Infinity;
        let currentNeighbors = graph[currentNode].neighbors
        
        // Visit the direct neighbours of the current node and add distances into current distances list
        for (let i=0; i<currentNeighbors.length; i++) {
        queue.push(currentNeighbors[i]);
        }
        
        while (queue.length > 0) {
        neighbor = queue.shift();
        neighborIndex = neighbor // // let's see for next league
        neighborDist = 1 // idem
            if (currentDist[currentNode] + neighborDist < currentDist[neighborIndex]) {
                currentDist[neighborIndex] = currentDist[currentNode] + neighborDist;

                shortesWayDict[neighborIndex].push( ...shortesWayDict[currentNode], neighborIndex)
            }
        }

        // Mark current node as visited
        visited.push(currentNode);

        //Chose the next node (the nearrest and non-visited from initial)
        for (let i in currentDist) {
            if (!visited.includes(i) && currentDist[i] < nextNodeDist) {
                nextNode = i;
                nextNodeDist = currentDist[i]
            }
        }
        currentNode = nextNode;
    }
    return({dist: currentDist, path: shortesWayDict})
}

const findDistance = (graph, nodeStart, nodeEnd) => {
    /* takes a graph and 2 nodes (int) & return the shortest distance between them (int) */
    let distList = dijkstraDistPath(graph, nodeStart).dist;
    let dist = distList[nodeEnd];
    return dist;
}

const findPath = (graph, nodeStart, nodeEnd) => {
    /* takes a graph and 2 nodes (int) & return the shortest distance between them (int) */
    let distList = dijkstraDistPath(graph, nodeStart).path;
    let path = distList[nodeEnd];
    return path;
}

const setTargetList = (graph, initialNode, type) => {
    /* takes a graph and and a initialNode index & return index of the nearest target (crystals or eggs) */

    // create a list of crystals cells
    let targetList = [] 
    for (let i=0; i<graph.length; i++) {
      if (graph[i].type === type && graph[i].resources > 0 ) {
        d = findDistance(graph, initialNode, i);
        r = graph[i].resources
        newTarget = [i, d, r]
        if (r > d) {
            targetList.push(newTarget)
        }
      }
    }
    // sort by ratio d/r
    targetList.sort((a, b) => a[1]/a[2] - b[1]/b[2]);

    return targetList; //[[index, dist, ressources], [], ...]
}

const createPath = (list, initialNode) => {
    /* takes a list structured like : [[index, dist, ressources], [], ...] & return an array with a path that link all list'node 
    use a "nearest neighbor approach" */

    let path = [];
    let subPath = [];
    currentNode = initialNode;
    path.push(currentNode);
    while (list.length > 0) {
      nextDestinationNode = list.shift()[0];
      subPath = findPath(graph, currentNode, nextDestinationNode);
      subPath.shift();
      path.push(...subPath);
      path = [...new Set(path)]; //remove duplicates

      currentNode = nextDestinationNode;
    }
    return path;
}

const createPathEggs = (graph, initialNode) => {
    /* takes a graph, a base index, a type (2:crytals 1:eggs) & return an array with a path that link all crystals 
    use a "nearest neighbor approach" */

    // create a list of crystals cells structured like : [[index, dist, ressources], [], ...]
    let targetList = setTargetList(graph, initialNode, 1);
    //limit to one egg node
    targetList = targetList.slice(0,1);
    // create a path between all crystals
    let path = createPath(targetList, initialNode);

    return path;
}

const createPathCrystals = (graph, initialNode) => {
    /* takes a graph, a base index, a type (2:crytals 1:eggs) & return an array with a path that link all crystals 
    use a "nearest neighbor approach" */

    // create a list of crystals cells structured like : [[index, dist, ressources], [], ...]
    let targetList = setTargetList(graph, initialNode, 2)
    //limit to one egg node
    if (targetList.length > 3) {
        targetList = targetList.slice(0, 3);
    }
    // create a path between all crystals
    let path = createPath(targetList, initialNode);

    return path;
}

const createPathMixed = (graph, initialNode) => {
    /* takes a graph, a base index, a type (2:crytals 1:eggs) & return an array with a path that link all crystals 
    use a "nearest neighbor approach" */

    // create a list of crystals cells structured like : [[index, dist, ressources], [], ...]
    let targetList = [] 
    for (let i=0; i<graph.length; i++) {
      if (graph[i].type === 1 || graph[i].type === 2 && graph[i].resources > 10 ) {
        d = findDistance(graph, initialNode, i);
        r = graph[i].resources
        newTarget = [i, d, r]
        if (r > d && r > 10) {
            targetList.push(newTarget)
        }
      }
    }
    targetList.sort((a, b) => a[1] - b[1]);

    //limit number of target
    if (targetList.length > 3) {
        targetList = targetList.slice(0, 3);
    }

    // create a path between all targets
    let path = createPath(targetList, initialNode);

    return path;
}

const isEggNextToMyAnts = (graph) => {
    let indexList = []
    for (let i=0; i<graph.length; i++) {
        if (graph[i].myAnts > 0) {
            for (let j=0; j<graph[i].neighbors.length; j++) {
                neighIndex = graph[i].neighbors[j];
                if (graph[neighIndex].type === 1) {
                    indexList.push(neighIndex)
                }
            }
        }
    }
    indexList = [...new Set(indexList)]; //remove duplicates

    let cellsWithMyAntsList = [];
    for (let i=0; i<indexList.length; i++) {
        eggIndex = indexList[i];
        let r = graph[eggIndex].resources;
        cellsWithMyAntsList.push([eggIndex, r])
    }
    cellsWithMyAntsList.sort((a, b) => a[1] + b[1])

    return cellsWithMyAntsList; //[[index, ressources], [], ...]
}

const eggsNextToBase = (graph, base) => {
    let indexList = [];
    neighList = graph[base].neighbors;
    for (let i=0; i<neighList.length; i++) {
        neighIndex = neighList[i];
        if (graph[neighIndex].type === 1 &&  graph[neighIndex].resources > 10) {
            indexList.push(neighIndex)
        }
    }
    return indexList;
}

// initial statement  --------------------------------------------------------------------------------------------------------
const graph = [];

const numberOfCells = parseInt(readline()); // amount of hexagonal cells in this map
for (let i = 0; i < numberOfCells; i++) {
    var inputs = readline().split(' ');
    const type = parseInt(inputs[0]); // 0 for empty, 1 for eggs, 2 for crystal
    const initialResources = parseInt(inputs[1]); // the initial amount of eggs/crystals on this cell
    const neigh0 = parseInt(inputs[2]); // the index of the neighbouring cell for each direction
    const neigh1 = parseInt(inputs[3]);
    const neigh2 = parseInt(inputs[4]);
    const neigh3 = parseInt(inputs[5]);
    const neigh4 = parseInt(inputs[6]);
    const neigh5 = parseInt(inputs[7]);

    const cell = {
        type,
        resources: initialResources,
        neighbors: [neigh0, neigh1, neigh2, neigh3, neigh4, neigh5].filter(id => id > -1),
        myAnts: 0,
        oppAnts: 0
      }

    graph.push(cell)
}

const numberOfBases = parseInt(readline());
const myBases = readline().split(' ').map(n => parseInt(n))
const oppBases = readline().split(' ').map(n => parseInt(n))

console.error("graph", graph);
console.error("myBases", myBases);
console.error("oppBases", oppBases);

// game loop --------------------------------------------------------------------------------------------------------
while (true) {
    for (let i = 0; i < numberOfCells; i++) {
        var inputs = readline().split(' ');
        const resources = parseInt(inputs[0]); // the current amount of eggs/crystals on this cell
        const myAnts = parseInt(inputs[1]); // the amount of your ants on this cell
        const oppAnts = parseInt(inputs[2]); // the amount of opponent ants on this cell

        graph[i].resources = resources
        graph[i].myAnts = myAnts
        graph[i].oppAnts = oppAnts
    }


   // create list of all eggs index next to base [index, index, ...]
   let eggsNextToBaseList = eggsNextToBase(graph, myBases[0]);

   // create list of all crystals [[index, dist, ressources], [], ...]
   let crystalList = setTargetList(graph, myBases[0], 2);
   let crystalLimit = 5;
   if (crystalList.length > crystalLimit) {
       crystalList = crystalList.slice(0, crystalLimit);
    }
    
    //create list of all eggs [[index, dist, ressources], [], ...]
    let eggList = setTargetList(graph, myBases[0], 1);
    let eggLimit = 2;
    if (eggList.length > eggLimit) {
        eggList = eggList.slice(0, eggLimit);
    }

    // create list of all eggs next to ants [[index, ressources], [], ...]
    let nearEggsList = isEggNextToMyAnts(graph);

    
    // set actions
    // WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    const actions = [];

    if (eggsNextToBaseList.length > 0) {
        for (let i=0; i<eggsNextToBaseList.length; i++) {
            actions.push([`LINE ${myBases[0]} ${eggsNextToBaseList[i]} 1`]); 
        }
    } else {
        for (let i=0; i<crystalList.length; i++) {
            actions.push([`LINE ${myBases[0]} ${crystalList[i][0]} 2`]); 
        }
        for (let i=0; i<eggList.length; i++) {
            actions.push([`LINE ${myBases[0]} ${eggList[i][0]} 2`]); 
        }
        for (let i=0; i<nearEggsList.length; i++) {
            actions.push([`BEACON ${nearEggsList[i][0]} 1`]); 
        }
    }

    // test = dijkstraDistPath(graph, myBases[0])
    // console.error(test)

    // TODO: choose actions to perform and push them into actions
    // To debug: console.error('Debug messages...');
    if (actions.length === 0) {
        console.log('WAIT');
    } else {
        console.log(actions.join(';'));
    }
}


