package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	fmt.Println("Hello from day12 in Go!")

	puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)

	if err != nil {
		log.Fatalln("Error: ", err.Error())
	}

	content := bytes.Split(c, []byte("\n"))
	nodes := make([][]string, 0)

	for _, line := range content {
		// lineStr := string(line)
		// fmt.Println(lineStr)
		tmp := strings.Split(string(line), "-")
		nodes = append(nodes, tmp)
	}

	for _, node := range nodes {
		fmt.Println(node)
	}
	// 1. build a graph with list
	// 2. list of visited nodes per each search
	// 3. list of already discovered paths
	// 4. it is a breadh first search algorithm
}
