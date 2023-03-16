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
    const MOVE: (u32, u32) = (3, 1);
    let mut x: u32 = 0;
    let mut y: u32 = 0;
    let mut trees_count: u32 = 0;
    let row_len = tree_map[0].len() as u32;
    for _row in &tree_map {
        if (y + MOVE.0) >= row_len {
            y = MOVE.0 - (row_len - y)
        }
        else {
            y = y + MOVE.0; 
        }
        x = x + MOVE.1;
        if x >= tree_map.len() as u32 {
            break;
        }
        if tree_map[x as usize][y as usize] == '#' {
            trees_count += 1;
        }
        //println!("The new coords are, row: {}, col: {} and square is: {}",
        //        x, y, tree_map[x as usize][y as usize]);
    }
    println!("The numbers of trees approached is: {}", trees_count);



}
