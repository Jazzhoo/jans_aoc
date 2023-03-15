use std::{fs, io::Read};
fn main() {
    let mut file = fs::File::open("src/example_input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.trim().split("\n").collect();
    let mut tree_map: Vec<Vec<char>> = Vec::new();
    let mut tree_map_bin: Vec<Vec<bool>> = Vec::new();

    for (idx, row) in data.iter().enumerate() {
        let row_conv: Vec<char> = row.chars().collect();
        tree_map_bin.push(Vec::new());
        for sqr in &row_conv {
            let mut sqr_bin = false;
            if *sqr == '#' {
                sqr_bin = true;
            }
            tree_map_bin[idx].push(sqr_bin);
        }
        tree_map.push(row_conv);
    }
    println!("{:?}", tree_map_bin);
    const MOVE = (3, 1);
    for (idx, row) in tree_map_bin.iter().enumerate() {
        
    }


}
