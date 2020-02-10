use std::fs;
    
fn step(memory: &mut Vec<i32>, ip: i32) -> bool {
    let instr = *&memory[ip as usize];
    let p1 = *&memory[(ip+1) as usize];
    let p2 = *&memory[(ip+2) as usize];
    let p3 = *&memory[(ip+3) as usize];
    if instr == 1 {
        memory[p3 as usize] = &memory[p1 as usize] + &memory[p2 as usize];
    }
    if instr == 2 {
        memory[p3 as usize] = &memory[p1 as usize] * &memory[p2 as usize];
    }
    if instr == 99 {
        return false;
    }
    true
}

fn run(memory: &mut Vec<i32>) -> i32 {
    let mut ip = 0;
    let mut con = step(memory, ip);
    while con {
        ip += 4;
        con = step(memory, ip);
    }
    memory[0]
}

fn run_nv(program: &Vec<i32>, noun: i32, verb: i32) -> i32 {
    let mut memory = program.to_vec();
    memory[1] = noun;
    memory[2] = verb;
    run(&mut memory)
}

fn part2(program: &Vec<i32>) -> i32 {
    for n in 0..100 {
        for v in 0..100 {
            let r = run_nv(program, n, v);
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
    let mut program: Vec<i32> = input.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    let part1 = run_nv(&mut program, 12, 2);
    println!("Day 02 part 1: {}", part1);
    let part2 = part2(&mut program);
    println!("Day 02 part 2: {}", part2);
}
