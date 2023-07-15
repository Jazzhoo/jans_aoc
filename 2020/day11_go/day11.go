package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
)

func duplicate_matrix(input_matrix [][]byte) [][]byte {
	temp_matrix := make([][]byte, len(input_matrix))
	for idx, row := range input_matrix {
		temp_matrix[idx] = make([]byte, len(row))
		copy(temp_matrix[idx], row)
	}
	return temp_matrix
}
func look_around(input_matrix [][]byte, x int, y int, max_x int, max_y int) int {
	var count int
	for i := range []int{-1, 0, 1} {
		new_y := y + i
		if new_y < 0 || new_y >= max_y {
			continue
		}
		for j := range []int{-1, 0, 1} {
			new_x := x + j
			if new_x == 0 && new_y == 0 {
				continue
			}
			if new_x < 0 || new_x >= max_x {
				continue
			}
			if input_matrix[new_y][new_x] == '#' {
				count++
			}

		}
	}

	return count
}

func main() {
	fmt.Println("Hello from day 11 of 2020 in GO!")

	puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("Error reading file: ", err.Error())
	}

	content := bytes.Split(c, []byte("\n"))
	content[0][0] = 'x'
	content2 := duplicate_matrix(content)
	content2[0][1] = 'y'

	fmt.Println("Testing with bytes")
	for _, line := range content {
		fmt.Printf("%s\n", string(line))
	}

	fmt.Println("Testing copy of slice of bytes")
	for _, line := range content2 {
		fmt.Printf("%s\n", string(line))
	}
}
