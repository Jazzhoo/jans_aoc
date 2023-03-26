use std::{fs, collections::HashMap};

#[derive(Debug)]
struct Instruction {
    moves: u32,
    from: u32,
    to: u32,
}

fn main() {
    let input_raw = fs::read_to_string("src/inputs/example_input.txt");
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
            //println!("temp_line: {:?}", temp_line);
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
    for key in crate_map.keys().copied() {
        crate_map.get_mut(&key).unwrap().reverse();

    }
    println!("before action {:?}", crate_map);

    for inst in instruction_raw {
        for _i in 0..inst.moves {
            let temp_chr = crate_map.get_mut(&inst.from).unwrap().pop().unwrap();
            crate_map.get_mut(&inst.to).unwrap().push(temp_chr);
            println!("{:?}", crate_map);
        }
    }
}
