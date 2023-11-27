package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"regexp"
)

func main() {
	puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("Cannot read file", err.Error())
	}
	content := bytes.Split(c, []byte("\n"))
	lineRe := regexp.MustCompile(`^(\D+)\s(\+|-)([0-9]+)$`)

	for _, line := range content {
		lineStr := string(line)
		match := lineRe.FindStringSubmatch(lineStr)

		fmt.Println(lineStr)
        fmt.Println(match[1:])
	}
}
