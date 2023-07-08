package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func findRow(code string) int {
	left := 0
	right := 127
	for _, c := range code {
		var middle int = (left + right + 1) / 2
		if c == 'B' {
			left = middle
		}
	}
	return 0
}

func findCol(code string) int {
	return 0
}

func main() {
	fmt.Println("Hello from day5")

	puzzle := "./input_files/example_puzzle.txt"
	// puzzle := "./input_files/main_puzzle.txt"

	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("Error reading file, ", err.Error())
	}

	content := strings.Split(string(c), "\n")

	for _, line := range content {
		// fmt.Printf("%d: %s ", idx, line)
		rowCode := line[:7]
		colCode := line[7:]
		fmt.Printf("L: %s; R: %s; C: %s\n", line, rowCode, colCode)
	}

}
