package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"regexp"
	"slices"
	"strconv"
)

type Instruction struct {
	direction string
	value     int
}

func checkMatrix(mat [][]uint8) int {
	var counter int
	for i := range mat {
		for j := range mat[0] {
			if mat[i][j] == 1 {
				counter++
			}
		}
	}
	return counter
}
func printMatrix(mat [][]uint8) {
	for i := range mat {
		for j := range mat[0] {
			if mat[i][j] == 0 {
				fmt.Print(" ")
			} else {
				fmt.Print("#")
			}
		}
		fmt.Print("\n")
	}
}
func fldMatrix(ins Instruction, mat [][]uint8) [][]uint8 {
	if ins.direction == "y" {
		var foldMatrix [][]uint8
		for _, row := range mat[ins.value+1:] {
			newRow := make([]uint8, len(row))
			copy(newRow, row)
			foldMatrix = append(foldMatrix, newRow)
		}
		slices.Reverse(foldMatrix)
		originalRemain := make([][]uint8, len(mat[:ins.value]), len(mat[:ins.value]))
		copy(originalRemain, mat[:ins.value])
		var newMatrix [][]uint8
		for _, row := range originalRemain {
			copyRow := make([]uint8, len(row))
			copy(copyRow, row)
			newMatrix = append(newMatrix, copyRow)
		}
		if len(originalRemain) >= len(foldMatrix) {
			whereToStart := len(originalRemain) - len(foldMatrix)
			for idx := whereToStart; idx < len(originalRemain); idx++ {
				for jdx := 0; jdx < len(originalRemain[0]); jdx++ {
					newMatrix[idx][jdx] = originalRemain[idx][jdx] + foldMatrix[idx-whereToStart][jdx]
					if newMatrix[idx][jdx] > 1 {
						newMatrix[idx][jdx] = 1
					}
				}
			}
		}
		return newMatrix
	} else {
		var foldMatrix [][]uint8
		originalRemain := make([][]uint8, len(mat), len(mat))
		for idx, row := range mat {
			newOrgRow := make([]uint8, len(row[:ins.value]))
			copy(newOrgRow, row[:ins.value])
			originalRemain[idx] = newOrgRow

			newRow := make([]uint8, len(row[ins.value+1:]))
			copy(newRow, row[ins.value+1:])
			slices.Reverse(newRow)
			foldMatrix = append(foldMatrix, newRow)
		}
		newMatrix := originalRemain
		if len(originalRemain[0]) >= len(foldMatrix[0]) {
			whereToStart := len(originalRemain[0]) - len(foldMatrix[0])
			for idx := 0; idx < len(foldMatrix); idx++ {
				for jdx := whereToStart; jdx < len(originalRemain[0]); jdx++ {
					newMatrix[idx][jdx] = originalRemain[idx][jdx] + foldMatrix[idx][jdx-whereToStart]
					if newMatrix[idx][jdx] > 1 {
						newMatrix[idx][jdx] = 1
					}
				}
			}
		}
		return newMatrix
	}
}

func main() {
	puzzle := "./input_files/main_puzzle.txt"
	// puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("error reading file")
	}
	content := bytes.Split(c, []byte("\n"))
	var coords [][]int
	var instr []Instruction
	var max_y, max_x int
	instrRe := regexp.MustCompile("fold along (x|y)=(\\d+)")
	for _, line := range content {
		if len(line) == 0 {
			continue
		} else if line[0] == 'f' {
			regexMatch := instrRe.FindStringSubmatch(string(line))
			if len(regexMatch) == 3 {
				intConv, err := strconv.Atoi(regexMatch[2])
				if err != nil {
					continue
				}
				instr = append(instr, Instruction{
					direction: regexMatch[1],
					value:     intConv,
				})
			}
		} else {
			splitLine := bytes.Split(line, []byte(","))
			_y, _ := strconv.Atoi(string(splitLine[1]))
			_x, _ := strconv.Atoi(string(splitLine[0]))
			coords = append(coords, []int{_x, _y})
			if _x > max_x {
				max_x = _x
			}
			if _y > max_y {
				max_y = _y
			}
		}

	}
	man := make([][]uint8, max_y+1)
	for c := range man {
		man[c] = make([]uint8, max_x+1)
	}
	for _, c := range coords {
		man[c[1]][c[0]] = 1
	}
	newMat := man
	for _, ins := range instr {
		newMat = fldMatrix(ins, newMat)
	}
    printMatrix(newMat)
}
