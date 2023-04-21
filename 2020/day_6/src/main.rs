use std::fs;
use std::collections::{HashSet, HashMap} ;

fn main() {
    //reading the datafile
    let raw_data = fs::read_to_string("src/input").expect("error while reading file");
    let data = raw_data.trim().split("\n\n").collect::<Vec<&str>>();
    let mut data_clear = Vec::new();
    for group in &data{
        data_clear.push(group.trim().split("\n").collect::<Vec<&str>>());
    }
    //println!("{:?}", data_clear);
    //let data = raw_data.trim().split("\n\n").map(|s| s.replace("\n", "")).collect::<Vec<String>>();
    let mut result = 0;
    let mut result_2 = 0;
    let mut ans_map = Vec::new();

// ===== Part 1==========
    for group in data_clear {
        let mut temp_set = HashSet::new();
        let mut temp_map = HashMap::new();

        for person in &group {
            for ans in person.chars() {
                temp_set.insert(ans);
                let count = temp_map.entry(ans).or_insert(0);
                *count += 1;
            }

        }
        ans_map.push(temp_map.clone());
        //println!("the qunique set of {:?}", group);
        //println!("is {:?}", temp_set);
        result += temp_set.len();
        for (_,val) in temp_map.into_iter() {
            result_2 += val / group.len();
        }
    println!("for group {:?}, len: {}, result_2: {}", group, group.len(), result_2);
    }
    println!("The part 1 solution is: {}", result);

    println!("The part 1 solution is: {}", result_2);

    

}
