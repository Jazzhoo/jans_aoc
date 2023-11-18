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

func appendPath(lop [][]string, pth []string) [][]string {
	internalPath := make([]string, len(pth))
	copy(internalPath, pth)
	lop = append(lop, internalPath)
	return lop
}
func main() {
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
	var pathsToFollow [][]string
	initialPath := []string{"start"}
	pathsToFollow = appendPath(pathsToFollow, initialPath)
	var pathsFound [][]string
	for {

    currentPath := pathsToFollow[len(pathsToFollow) - 1]
    pathsToFollow = pathsToFollow[:len(pathsToFollow) - 1:len(pathsToFollow) - 1]
		currentCave := currentPath[len(currentPath)-1]
		// fmt.Printf("The current path is: %v\n", currentPath)
		// fmt.Printf("from %s i see: %v\n", currentCave, caveMap[currentCave])
		for _, nextCave := range caveMap[currentCave] {
			var newPath []string
			newPath = currentPath
			newPath = append(newPath, nextCave)
			// fmt.Printf("NewPath: %v\n", newPath.caves)

			if nextCave == "end" {
				// fmt.Printf("====>> Adding %v to the paths found\n", newPath)
				pathsFound = appendPath(pathsFound, newPath)
				continue
			}
			if unicode.IsUpper(rune(nextCave[0])) || !slices.Contains(currentPath, nextCave) {
				// fmt.Printf("NewPath inside if: %v\n", newPath)
				// fmt.Printf("Adding %v to the paths to follow\n", newPath)
				pathsToFollow = appendPath(pathsToFollow, newPath)
			}
		}
		// fmt.Printf("Next paths: %v\n", pathsToFollow)
		// fmt.Println("======\n")
		// time.Sleep(1 * time.Second)
		if len(pathsToFollow) == 0 {
			break
		}
	}
	fmt.Printf("All paths found: %d\n", len(pathsFound))
}
