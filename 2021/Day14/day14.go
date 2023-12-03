package main

import (
	"bytes"
	"fmt"
	"log"
	"math"
	"os"
)

func initalPolymer(base string) map[string]int {
	polymer := make(map[string]int)
	for idx := 0; idx < len(base)-1; idx++ {
		newPair := string(base[idx]) + string(base[idx+1])
		polymer[newPair]++
	}
	return polymer
}
func polymerization(base map[string]int, rules map[string]string, lastElement string) (map[string]int, map[string]int) {
	newPolymer := make(map[string]int)
	elementsCount := make(map[string]int)
	for key := range base {
		pair1 := string(string(key[0]) + rules[key])
		pair2 := string(rules[key] + string(key[1]))
		newPolymer[pair1] += base[key]
		newPolymer[pair2] += base[key]
		elementsCount[string(pair1[0])] += base[key]
		elementsCount[string(pair1[1])] += base[key]
	} // add last element
	elementsCount[lastElement]++
	return newPolymer, elementsCount
}
func main() {
	puzzle := "./input_files/main_puzzle.txt"
	// puzzle := "./input_files/example_puzzle.txt"
	c, err := os.ReadFile(puzzle)
	if err != nil {
		log.Fatalln("error reading file")
	}
	content := bytes.Split(c, []byte("\n"))

	polymerTemplate := string(content[0])
	rules := make(map[string]string)
	for idx := 2; idx < len(content); idx++ {
		if string(content[idx]) == "" {
			continue
		}
		lineSplit := bytes.Split(content[idx], []byte(" -> "))
		rules[string(lineSplit[0])] = string(lineSplit[1])
	}

	iterationPolymer := initalPolymer(polymerTemplate)
	elementsCount := make(map[string]int)
	for idx := 0; idx < 40; idx++ {
		iterationPolymer, elementsCount = polymerization(iterationPolymer, rules, string(polymerTemplate[len(polymerTemplate)-1]))
	}
	min := math.MaxInt
	max := 0

	for _, v := range elementsCount {
		if min > v {
			min = v
		}
		if max < v {
			max = v
		}
	}
	fmt.Printf("The result is: %d\n", max-min)
}
