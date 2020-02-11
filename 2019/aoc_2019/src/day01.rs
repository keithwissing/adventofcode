use std::fs;

/// Calculate fuel for mass
///
/// # Examples
///
/// ```
/// let result = day01::fuel(&100756);
/// assert_eq!(result, 33583);
/// ```
fn fuel(x: &i32) -> i32 {
    let ret = x / 3 - 2;
    ret
}

fn plus_fuel(x: &i32) -> i32 {
    let mut total = fuel(x);
    let mut more = fuel(&total);
    while more > 0 {
        total = total + more;
        more = fuel(&more);
    }
    total
}

pub fn day01() {
    let filename = "../day01_input.txt";
    let input = fs::read_to_string(filename).expect("Could not read file");
    let values: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    let part1: i32 = values.iter().map(fuel).sum();
    println!("Day 01 Part 1 answer: {}", part1);
    let part2: i32 = values.iter().map(plus_fuel).sum();
    println!("Day 01 Part 2 answer: {}", part2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fuel() {
        assert_eq!(fuel(&12), 2);
        assert_eq!(fuel(&14), 2);
        assert_eq!(fuel(&1969), 654);
        assert_eq!(fuel(&100756), 33583);
    }

    #[test]
    fn test_plus_fuel() {
        assert_eq!(plus_fuel(&14), 2);
        assert_eq!(plus_fuel(&1969), 966);
        assert_eq!(plus_fuel(&100756), 50346);
    }
}
