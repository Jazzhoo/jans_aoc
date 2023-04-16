use std::fs;

fn main() {
    let raw_data = fs::read_to_string("src/input").expect("error while reading file");
    let raw_data = raw_data.trim().split("\n").collect::<Vec<&str>>();
    println!("{:?}", raw_data);
    let mut the_biggest_id: u32 = 0;


    for pass in &raw_data {
        let row_raw = &pass.chars().collect::<Vec<char>>()[..7];
        let col_raw = &pass.chars().collect::<Vec<char>>()[7..];
        println!("row: {:?}, col: {:?}", row_raw, col_raw);
        let mut seat_id: u32 = 0;
        let mut col_id: u32 =0;

        for (idx, chr) in row_raw.iter().enumerate() {
            let pow = row_raw.len() - 1;
            seat_id += match chr {
                'B' => {
                    u32::pow(2, (pow - idx) as u32)
                },
                'F' => {0},
                _ => 0,
            };
            println!("pow: {}, idx: {}, seat_id: {}", pow, idx, seat_id);
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
        let result = seat_id * 8 + col_id;
        if result > the_biggest_id {
            the_biggest_id = result;
        }
        println!("seat_id: {}, col_id: {}, result: {}", seat_id, col_id, result);

    }
    println!("The result of part1 is {}", the_biggest_id);

}
