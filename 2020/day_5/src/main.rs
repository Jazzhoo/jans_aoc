use std::fs;

fn translate_seat_id(raw_seat_id: &str) -> (u32, u32, u32) {
    let row_raw = &raw_seat_id.chars().collect::<Vec<char>>()[..7];
    let col_raw = &raw_seat_id.chars().collect::<Vec<char>>()[7..];
    println!("row: {:?}, col: {:?}", row_raw, col_raw);
    let mut row_id: u32 = 0;
    let mut col_id: u32 =0;

    for (idx, chr) in row_raw.iter().enumerate() {
        let pow = row_raw.len() - 1;
        row_id += match chr {
            'B' => {
                u32::pow(2, (pow - idx) as u32)
            },
            'F' => {0},
            _ => 0,
        };
        println!("pow: {}, idx: {}, row_id: {}", pow, idx, row_id);
    }
    for (idx, chr) in col_raw.iter().enumerate() {
        let pow = col_raw.len() - 1;
        col_id += match chr {
            'R' => {
                u32::pow(2, (pow - idx) as u32)
            },
            'L' => {0},
            _ => 0,
        };
        println!("pow: {}, idx: {}, col_id: {}", pow, idx, col_id);
    }
    let seat_id =  row_id * 8 + col_id;
    return ( row_id, col_id, seat_id);
}

fn main() {
    let raw_data = fs::read_to_string("src/input").expect("error while reading file");
    let raw_data = raw_data.trim().split("\n").collect::<Vec<&str>>();
    println!("{:?}", raw_data);
    let mut the_biggest_id: u32 = 0;
    let mut all_ids = Vec::new();


    for pass in &raw_data {
        let result = translate_seat_id(&pass);
        if result.2 > the_biggest_id {
            the_biggest_id = result.2;
        }
        all_ids.push(result.2);
    }
    println!("The result of part1 is {}", the_biggest_id);
    for seat_id in *all_ids.iter().min().unwrap()..*all_ids.iter().max().unwrap() {
        if !all_ids.contains(&seat_id) {
            println!("..and part2 is {}", seat_id);
        }
    }

}
