package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"strings"
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
			count++
		}
	}
	return count
}
func dfs(pth Path, caveMap map[string][]string) []Path {
	var out []Path
	currentCave := pth.caves[len(pth.caves)-1]
	// fmt.Printf("I'm in: %v\n", currentCave)
	for _, cave := range caveMap[currentCave] {
		intPth := Path{
            caves : make([]string, len(pth.caves)),
            doubled: false,
        }
        copy(intPth.caves, pth.caves)
		intPth.caves = append(intPth.caves, cave)
		if cave == "end" {
			// fmt.Printf("Found end path: %v\n", intPth)
			out = append(out, intPth)
		} else if unicode.IsUpper(rune(cave[0])) || caveCount(pth, cave) == 0 {
			out = append(out, dfs(intPth, caveMap)...)
		}
	}
	return out
}

func main() {
	puzzle := "./input_files/main_puzzle.txt"
	// puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("error reading file")
	}

	content := bytes.Split(c, []byte("\n"))
	caveMap := map[string][]string{}

	for _, line := range content {
		edge := strings.Split(string(line), "-")
		caveMap[edge[0]] = append(caveMap[edge[0]], edge[1])
		caveMap[edge[1]] = append(caveMap[edge[1]], edge[0])
	}

	initialPath := Path{
		caves:   []string{"start"},
		doubled: false,
	}
	foundPaths := dfs(initialPath, caveMap)
	fmt.Printf("len of paths found: %d\n", len(foundPaths))
	// for idx, path := range foundPaths {
	// 	fmt.Printf("%d: %v\n", idx+1, path)

	// }

}
