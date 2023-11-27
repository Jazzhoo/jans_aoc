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

type Path struct {
	caves   []string
	doubled bool
}

func appendPath(lop []Path, pth Path) []Path {
	internalPath := Path{
		caves:   make([]string, len(pth.caves)),
		doubled: pth.doubled,
	}
	copy(internalPath.caves, pth.caves)
	lop = append(lop, internalPath)
	return lop
}
func caveCount(pth Path, cve string) int {
    count := 0
    for _, cave := range pth.caves {
        if cave == cve {
            count ++
        }

    }
    return count
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

	// fmt.Printf("Small caves: %v\n", smallCaves)
	var pathsFound []Path

	var pathsToFollow []Path
	initialPath := Path{
		caves:   []string{"start"},
		doubled: false,
	}
	pathsToFollow = appendPath(pathsToFollow, initialPath)
	// var currentPath Path
	for {
        // fmt.Printf("Paths to follow: %v\n", pathsToFollow)
        currentPath := pathsToFollow[len(pathsToFollow)-1]
		pathsToFollow = pathsToFollow[: len(pathsToFollow)-1 : len(pathsToFollow)-1]
		currentCave := currentPath.caves[len(currentPath.caves)-1]
		// fmt.Printf("The current path is: %v\n", currentPath)
		// fmt.Printf("from %s i see: %v\n", currentCave, caveMap[currentCave])
		for _, nextCave := range caveMap[currentCave] {
            newPath := currentPath
			newPath.caves = append(newPath.caves, nextCave)
			// fmt.Printf("NewPath: %v\n", newPath.caves)

			if nextCave == "end" {
				// fmt.Printf("====>> Adding %v to the paths found\n", newPath)
				pathsFound = appendPath(pathsFound, newPath)
				continue
			} else if unicode.IsUpper(rune(nextCave[0])) || !slices.Contains(currentPath.caves, nextCave) {
				// fmt.Printf("NewPath inside if: %v\n", newPath)
				pathsToFollow = appendPath(pathsToFollow, newPath)
			} else if !currentPath.doubled && caveCount(currentPath, nextCave) == 1 && nextCave != "start"{
                newPath.doubled = true
                // fmt.Printf("Adding to the paths to follow: %v\n", newPath)
				pathsToFollow = appendPath(pathsToFollow, newPath)
                // fmt.Printf("Added path: %v\n", pathsToFollow[len(pathsToFollow) -1])
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
	// for idx, path := range pathsFound {
	// 	fmt.Printf("%d: %v\n", idx, path)
	// }
}
