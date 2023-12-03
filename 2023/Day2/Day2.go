package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
)

func validateGame(template map[string]int, game map[string]int) bool {
    valid := true
    for k := range game {
        if template[k] < game[k] {
            valid = false
        }
    }
    return valid

}
func main() {
    fmt.Println("Ho ho ho, day2 2023!")

    //reading the file
    puzzle := "./input_files/main_puzzle.txt"
    // puzzle := "./input_files/example_puzzle.txt"
    c, err := os.ReadFile(puzzle)
    if err != nil {
        log.Fatalln("error while reading file")
    }

    //maps declaration
    templateMap := map[string]int {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    games := make([]map[string]int, 1) //risky move 

    content := bytes.Split(c, []byte("\n"))
    for _, line := range content {
        if string(line) == "" {
            continue
        }
        game := bytes.Split(line, []byte(": "))
        game = bytes.Split(game[1], []byte("; "))
        gameMap := make(map[string]int)
        for _, pull := range game {
            cubes := bytes.Split(pull, []byte(", "))
            for _, color := range cubes {
                counts := bytes.Split(color, []byte(" "))
                colorStr := string(counts[1])
                intNum, err := strconv.Atoi(string(counts[0]))
                if err != nil {
                    log.Fatalf("Cannot convert %v to int\n", string(counts[0]))
                }
                if intNum > gameMap[colorStr] {
                    gameMap[colorStr] = intNum
                } 
            }
        }
        games = append(games, gameMap)

        // lineStr := string(lineSplit[0])
        // fmt.Println(lineStr)
    }
    // fmt.Println("Template")
    // fmt.Println(templateMap)
    // fmt.Println("games")
    // fmt.Println(games)
    var sumOfIDs int
    var sumOfPows int
    for idx := 1; idx<len(games); idx++ {
        if validateGame(templateMap, games[idx]) {
            sumOfIDs += idx
        }
        localPow := 1
        for _, v := range games[idx] {
            localPow *= v
        }
        sumOfPows += localPow
    }
    fmt.Printf("The result 1: is: %d\n", sumOfIDs)
    fmt.Printf("The result 2: is: %d\n", sumOfPows)
    
}
