use std::{fs, collections::HashMap};

#[derive(Debug)]
struct Instruction {
    moves: u32,
    from: u32,
    to: u32,
}

fn main() {
    let input_raw = fs::read_to_string("src/inputs/input.txt");
    let input_raw = match input_raw {
        Ok(file) => file,
        Err(err) => panic!("error occured {:?}", err),
    };
    let input = input_raw.split("\n").collect::<Vec<&str>>();
    let mut crate_map_raw: Vec<Vec<char>> = Vec::new();
    let mut instruction_raw: Vec<Instruction> = Vec::new();
    let mut crate_map: HashMap<u32, Vec<char>> = HashMap::new();

    for line in input {
        if line.contains('[') {
            crate_map_raw.push(line.chars().collect());
        }
        else if line.contains("move") {
            let temp_line: Vec<&str> = line.split_whitespace().collect();
            instruction_raw.push(Instruction { 
                moves: temp_line[1].parse().unwrap(), 
                from: temp_line[3].parse().unwrap(), 
                to: temp_line[5].parse().unwrap()})
        }
    }
    for row in crate_map_raw {
        let row_len = row.len();
        let mut key: u32 = 0;
        for idx in (1..row_len).step_by(4) {
            key += 1;
            if row[idx].is_alphabetic() {
                crate_map.entry(key).or_insert(Vec::new()).push(row[idx]);
            }
        }
    }
    let keys: Vec<u32> = crate_map.keys().cloned().collect();
    for key in &keys {
        crate_map.get_mut(&key).unwrap().reverse();
    }
    let mut crate_map_2 = crate_map.clone();
    //println!("before action {:?}", crate_map);
    for inst in &instruction_raw {
        for _i in 0..inst.moves {
            let temp_chr = crate_map.get_mut(&inst.from).unwrap().pop().unwrap();
            crate_map.get_mut(&inst.to).unwrap().push(temp_chr);
        }
    }
    //println!("after action {:?}", crate_map);
    let mut result = String::new();
    for i in 1..=*keys.iter().max().unwrap() {
        result.push(crate_map.get(&i).unwrap().last().unwrap().clone());
    }

    println!("====Part 1 ====");
    println!("The result is: {}", &result);

    for inst in &instruction_raw {
        let mut temp_chr: Vec<char> = Vec::new();
        for _i in 0..inst.moves {
            temp_chr.push(crate_map_2.get_mut(&inst.from).unwrap().pop().unwrap());
        }
        temp_chr.reverse();
        crate_map_2.get_mut(&inst.to).unwrap().append(&mut temp_chr);
    }
    //println!("after action {:?}", crate_map);
    let mut result = String::new();
    for i in 1..=*keys.iter().max().unwrap() {
        result.push(crate_map_2.get(&i).unwrap().last().unwrap().clone());
    }
    println!("====Part 2 ====");
    println!("The result is: {}", &result);
}
