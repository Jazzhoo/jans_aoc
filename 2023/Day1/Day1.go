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

func main() {
	puzzle := "./input_files/main_puzzle.txt"
	// puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("error reading file")
	}

	content := bytes.Split(c, []byte("\n"))
	digitMap := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
		"1":     "1",
		"2":     "2",
		"3":     "3",
		"4":     "4",
		"5":     "5",
		"6":     "6",
		"7":     "7",
		"8":     "8",
		"9":     "9",
	}
	reversedDigitMap := make(map[string]string)
	var digitRegex string
	var reversedDigitRegex string
	for k, v := range digitMap {
		rk := []rune(k)
		slices.Reverse(rk)
		digitRegex += k + "|"
		reversedDigitRegex += string(rk) + "|"
		reversedDigitMap[string(rk)] = v
	}
	digitRegex = digitRegex[:len(digitRegex)-1]
	reversedDigitRegex = reversedDigitRegex[:len(reversedDigitRegex)-1]
	// fmt.Println(digitRegex)
	// fmt.Println(reversedDigitRegex)
	var calibration int
	instrRe := regexp.MustCompile(digitRegex)
	instrReRe := regexp.MustCompile(reversedDigitRegex)
	for _, line := range content {
		if string(line) == "" {
			continue
		}
		revLine := make([]byte, len(line))
        copy(revLine, line)
		slices.Reverse(revLine)
		regexMatch1 := instrRe.FindString(string(line))
		regexMatch2 := instrReRe.FindString(string(revLine))

		// fmt.Println(string(line))
		// fmt.Println(string(revLine))
		// fmt.Println(regexMatch1)
		// fmt.Println(regexMatch2)
		strNum1 := digitMap[regexMatch1]
		strNum2 := reversedDigitMap[regexMatch2]
		// fmt.Println(strNum1)
		// fmt.Println(strNum2)
        strNum := strNum1 + strNum2
        intNum, _ := strconv.Atoi(strNum)
        calibration += intNum
		// fmt.Printf("Calibration is: %d\n", calibration)
	}
	fmt.Printf("The part 1 result is: %d\n", calibration)
}
