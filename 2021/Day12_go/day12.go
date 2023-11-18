package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
	// "time"
	"unicode"
)

func TakeOne(stack [][]string) []string {
	elementToPop := stack[len(stack)-1]
	return elementToPop
}

type Path struct {
	caves []string
}
type ListOfPaths struct {
	paths []Path
}

func (lop *ListOfPaths) appendPath(path Path) {
	var internalPath Path
	// fmt.Printf("internalPath len: %d, cap: %d\n", len(internalPath.caves), cap(internalPath.caves))
	internalPath.caves = append(internalPath.caves, path.caves...)
	// fmt.Printf("Inside the append: %v\n", path.caves)
	lop.paths = append(lop.paths, internalPath)
}

func (lop *ListOfPaths) pop() Path {
	lastPath := lop.paths[len(lop.paths)-1]
	var extractedPath Path
	extractedPath.caves = make([]string, len(lastPath.caves))
	copy(extractedPath.caves, lastPath.caves)
	newLopPathslen := len(lop.paths) - 1
	lop.paths = lop.paths[:newLopPathslen:newLopPathslen]

	return extractedPath
}

func main() {
	fmt.Println("Hello from day12 in Go!\n")

	puzzle := "./input_files/main_puzzle.txt"
	// puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)

	if err != nil {
		log.Fatalln("Error: ", err.Error())
	}

	content := bytes.Split(c, []byte("\n"))
	caveMap := map[string][]string{}

	// fmt.Println("== Building nodes ==")
	for _, line := range content {
		// fmt.Printf("raw: %v\n", string(line))
		edge := strings.Split(string(line), "-")
		// fmt.Printf("tmp: %v\n", edge)
		caveMap[edge[0]] = append(caveMap[edge[0]], edge[1])
		caveMap[edge[1]] = append(caveMap[edge[1]], edge[0])
	}
	// fmt.Println("== Done building nodes ==\n")

	// fmt.Print("Cave map: ")
	// fmt.Println(caveMap)

	var pathsToFollow ListOfPaths
	var initialPath Path
	initialCave := "start"
	initialPath.caves = append(initialPath.caves, initialCave)
	pathsToFollow.paths = append(pathsToFollow.paths, initialPath)
	var pathsFound ListOfPaths

	// fmt.Println("\n=== Entering the loop ===")
	// fmt.Println("\n=== checking the memory ===")
	// fmt.Printf("Initial cave: \t\t%v\n", &initialCave)
	// fmt.Printf("The starting point: \t%v\n", &initialPath.caves[0])
	// fmt.Printf("Paths to follow: \t%v\n", &pathsToFollow.paths[0].caves[0])

	for {

		currentPath := pathsToFollow.pop()
		currentCave := currentPath.caves[len(currentPath.caves)-1]
		// fmt.Printf("The current path is: %v\n", currentPath.caves)

		// fmt.Printf("from %s i see: %v\n", currentCave, caveMap[currentCave])
		for _, nextCave := range caveMap[currentCave] {
			var newPath Path
			newPath = currentPath
			newPath.caves = append(newPath.caves, nextCave)
			// fmt.Printf("NewPath: %v\n", newPath.caves)

			if nextCave == "end" {
				// fmt.Printf("====>> Adding %v to the paths found\n", newPath)
				pathsFound.appendPath(newPath)
				continue
			}
			if unicode.IsUpper(rune(nextCave[0])) || !slices.Contains(currentPath.caves, nextCave) {
				// fmt.Printf("NewPath inside if: %v\n", newPath.caves)
				// fmt.Printf("Adding %v to the paths to follow\n", newPath)
				pathsToFollow.appendPath(newPath)
			} else {
				// fmt.Printf("Doing nothing with: %s\n", nextCave)
			}

		}
		// fmt.Printf("Next paths: %v\n", pathsToFollow.paths)
		// fmt.Println("======\n")
		// time.Sleep(1 * time.Second)
		if len(pathsToFollow.paths) == 0 {
			break
		}
	}
  fmt.Printf("All paths found: %d\n", len(pathsFound.paths))
	// for idx, path := range pathsFound.paths {
	// 	fmt.Printf("%d: %v\n", idx, path)
	// }

	//
	// 1. build a graph with list
	// 2. list of visited nodes per each search
	// 3. list of already discovered paths
	// 4. it is a breadh first search algorithm
}
