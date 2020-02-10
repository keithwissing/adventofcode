use std::fs;
use std::collections::HashMap;

fn parameter(p: i32, memory: &HashMap<i32, i32>, ip:&i32) -> i32{
    let pv = match memory.get(&(ip + p)) {
        None => -1,
        Some(v) => *v
    };
    pv
}

fn grr(memory: &HashMap<i32, i32>, ip:&i32) -> i32 {
    parameter(0, memory, ip)
}

fn step(memory: &mut HashMap<i32, i32>, ip:&i32) -> bool {
    let instruction = parameter(0, memory, ip);
    let p1 = parameter(1, memory, ip);
    let p2 = parameter(2, memory, ip);
    let p3 = parameter(3, memory, ip);
    let v1 = grr(memory, &p1);
    let v2 = grr(memory, &p2);
    if instruction == 1 {
        memory.insert(p3, v1+v2);
    }
    if instruction == 2 {
        memory.insert(p3, v1*v2);
    }
    if instruction == 99 {
        return false
    }
    true
}

fn run(memory: &mut HashMap<i32, i32>) -> i32 {
    let mut ip = 0;
    let mut con = step(memory, &ip);
    while con {
        ip += 4;
        con = step(memory, &ip);
    }
    grr(memory, &0)
}

fn run_nv(program: &HashMap<i32, i32>, noun: i32, verb: i32) -> i32 {
    let mut memory = program.clone();
    memory.insert(1, noun);
    memory.insert(2, verb);
    run(&mut memory)
}

fn part2(memory: &HashMap<i32, i32>) -> i32 {
    for n in 0..100 {
        for v in 0..100 {
            let r = run_nv(memory, n, v);
            if r == 19690720 {
                return n * 100 + v
            }
        }
    }
    0
}

pub fn day02() {
    let filename = "../day02_input.txt";
    let input = fs::read_to_string(filename)
        .expect("Could not read file");
    let values: Vec<i32> = input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    let mut memory = HashMap::new();
    for (i, v) in values.iter().enumerate() {
        memory.insert(i as i32, *v);
    }
    let part1 = run_nv(&mut memory, 12, 2);
    println!("Day 02 part 1: {}", part1);
    let part2 = part2(&mut memory);
    println!("Day 02 part 2: {}", part2);
}
