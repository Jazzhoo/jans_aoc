use std::fs;
use std::collections::HashSet;

fn main() {
    //reading the datafile
    let raw_data = fs::read_to_string("src/input").expect("error while reading file");
    let data = raw_data.trim().split("\n\n").map(|s| s.replace("\n", "")).collect::<Vec<String>>();
    let mut result = 0;
    println!("{:?}", data);

    for group in data {
        let mut temp_set = HashSet::new();
        for chr in group.chars() {
            temp_set.insert(chr);
        }
        println!("the qunique set of {:?}", group);
        println!("is {:?}", temp_set);
        result += temp_set.len();
    }
    println!("The part 1 solution is: {}", result);

}
