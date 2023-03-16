use std::{fs, io::Read};
fn main() {
    let mut file = fs::File::open("src/input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.trim().split("\n").collect();
    let mut tree_map: Vec<Vec<char>> = Vec::new();
    //let mut tree_map_bin: Vec<Vec<bool>> = Vec::new();

    for row in data {
        let row_conv: Vec<char> = row.chars().collect();
        tree_map.push(row_conv);
    }
    //println!("{:?}", tree_map);
    const MOVES: [(u32, u32); 5] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let mut x: u32 = 0;
    let mut y: u32 = 0;
    let mut trees_count: u32 = 0;
    let row_len = tree_map[0].len() as u32;
    for _row in &tree_map {
        if (y + MOVES[1].0) >= row_len {
            y = MOVES[1].0 - (row_len - y)
        }
        else {
            y = y + MOVES[1].0; 
        }
        x = x + MOVES[1].1;
        if x >= tree_map.len() as u32 {
            break;
        }
        if tree_map[x as usize][y as usize] == '#' {
            trees_count += 1;
        }
    }
    println!("====Part 1====");
    println!("The numbers of trees approached is: {}", trees_count);
    println!("====Part 2====");

    let mut result: u64 = 1;

    for slope in MOVES {
        x = 0;
        y = 0;
        trees_count = 0;

        for _row in &tree_map {
            if (y + slope.0) >= row_len {
                y = slope.0 - (row_len - y)
            }
            else {
                y = y + slope.0; 
            }
            x = x + slope.1;
            if x >= tree_map.len() as u32 {
                break;
            }
            if tree_map[x as usize][y as usize] == '#' {
                trees_count += 1;
            }
        }
        result *= trees_count as u64;
        println!("The # of trees is: {}", trees_count);
    }
    println!("The result is {}", result);
}
