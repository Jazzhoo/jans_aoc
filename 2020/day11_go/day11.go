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
	for _, i := range []int{-1, 0, 1} {
		new_y := y + i
		if new_y < 0 || new_y >= max_y {
			continue
		}
		for _, j := range []int{-1, 0, 1} {
			new_x := x + j
			if new_x == x && new_y == y {
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

func look_further(input_matrix [][]byte, col int, row int, max_col int, max_row int) int {
	moves := [][]int{{0, -1}, {0, 1}, {1, 1}, {1, -1}, {-1, 1}, {1, 0}, {-1, 0}, {-1, -1}}
	var count int

	for _, move := range moves {
		new_col := col + move[0]
		new_row := row + move[1]

		if new_col < 0 || new_col >= max_col {
			continue
		}
		if new_row < 0 || new_row >= max_row {
			continue
		}
		see_seat := input_matrix[new_row][new_col]
		see_seat_str := string(see_seat)
		_ = see_seat_str

		for see_seat == '.' {
			new_col += move[0]
			new_row += move[1]

			if new_col < 0 || new_col >= max_col {
				break
			}
			if new_row < 0 || new_row >= max_row {
				break
			}
			see_seat = input_matrix[new_row][new_col]
		}

		if see_seat == '#' {
			count++
			// fmt.Printf("Found # at: [%d, %d]\n", new_x, new_y)
		}
	}
	return count
}

func main() {
	fmt.Println("Hello from day 11 of 2020 in GO!")

	// puzzle := "./input_files/example_puzzle.txt"
	puzzle := "./input_files/main_puzzle.txt"

	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("Error reading file: ", err.Error())
	}

	current_matrix := bytes.Split(c, []byte("\n"))
	max_row := len(current_matrix)
	max_col := len(current_matrix[0])
	backup_matrix := duplicate_matrix(current_matrix)
	next_matrix := duplicate_matrix(current_matrix)

	fmt.Println("Max row: ", max_row)
	fmt.Println("Max col: ", max_col)

	// fmt.Println("Current matrix")
	// for _, line := range current_matrix {
	// 	fmt.Printf("%s\n", string(line))
	// }

	var changes int
	for {
		changes = 0
		// for row, _ := range current_matrix {
		for row := 0; row < max_row; row++ {
			for col := 0; col < max_col; col++ {
				if current_matrix[row][col] == 'L' {
					seats_taken := look_around(current_matrix, col, row, max_col, max_row)
					if seats_taken == 0 {
						next_matrix[row][col] = '#'
						changes++
					}
				} else if current_matrix[row][col] == '#' {
					seats_taken := look_around(current_matrix, col, row, max_col, max_row)
					if seats_taken >= 4 {
						next_matrix[row][col] = 'L'
						changes++
					}
				}
			}
		}
		if changes == 0 {
			break
		}
		// fmt.Println("\nNext matrix")
		// for _, line := range next_matrix {
		// 	fmt.Printf("%s\n", string(line))
		// }
		current_matrix = duplicate_matrix(next_matrix)
	}
	var result1 int
	for row := 0; row < max_row; row++ {
		for col := 0; col < max_col; col++ {
			if next_matrix[row][col] == '#' {
				result1++
			}
		}
	}
	fmt.Printf("\nPart 1 result is: %d.\n ", result1)

	current_matrix = duplicate_matrix(backup_matrix)
	next_matrix = duplicate_matrix(current_matrix)
	// fmt.Println("Current matrix")
	// for _, line := range current_matrix {
	// 	fmt.Printf("%s\n", string(line))
	// }

	for {
		changes = 0
		// for row, _ := range current_matrix {
		for row := 0; row < max_row; row++ {
			for col := 0; col < max_col; col++ {
				if current_matrix[row][col] == 'L' {
					seats_taken := look_further(current_matrix, col, row, max_col, max_row)
					if seats_taken == 0 {
						next_matrix[row][col] = '#'
						changes++
					}
				} else if current_matrix[row][col] == '#' {
					seats_taken := look_further(current_matrix, col, row, max_col, max_row)
					if seats_taken >= 5 {
						next_matrix[row][col] = 'L'
						changes++
					}
				}
			}
		}
		if changes == 0 {
			break
		}
		// fmt.Println("\nNext matrix")
		// for _, line := range next_matrix {
		// 	fmt.Printf("%s\n", string(line))
		// }
		current_matrix = duplicate_matrix(next_matrix)
	}
	var result2 int
	for row := 0; row < max_row; row++ {
		for col := 0; col < max_col; col++ {
			if next_matrix[row][col] == '#' {
				result2++
			}
		}
	}
	fmt.Printf("\nPart 2 result is: %d.\n ", result2)

}
