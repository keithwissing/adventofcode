fn step(memory: &mut Vec<i32>, ip: i32) -> bool {
    let instr = *&memory[ip as usize];
    if instr == 99 {
        return false;
    }
    let p1 = *&memory[(ip + 1) as usize];
    let p2 = *&memory[(ip + 2) as usize];
    let p3 = *&memory[(ip + 3) as usize];
    if instr == 1 {
        memory[p3 as usize] = &memory[p1 as usize] + &memory[p2 as usize];
    }
    if instr == 2 {
        memory[p3 as usize] = &memory[p1 as usize] * &memory[p2 as usize];
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
                return n * 100 + v;
            }
        }
    }
    0
}

pub fn day02(program: &[i32]) -> (i32, i32) {
    let p1 = run_nv(&program.to_vec(), 12, 2);
    let p2 = part2(&program.to_vec());
    (p1, p2)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn array_to_vec(arr: &[i32]) -> Vec<i32> {
        arr.iter().cloned().collect()
    }

    fn test_run(program: &[i32], expected: &[i32]) {
        let mut memory = array_to_vec(program);
        run(&mut memory);
        assert_eq!(memory, expected);
    }

    #[test]
    fn test_small_programs() {
        test_run(&[1, 0, 0, 0, 99], &[2, 0, 0, 0, 99]);
        test_run(&[2, 3, 0, 3, 99], &[2, 3, 0, 6, 99]);
        test_run(&[2, 4, 4, 5, 99, 0], &[2, 4, 4, 5, 99, 9801]);
        test_run(
            &[1, 1, 1, 4, 99, 5, 6, 0, 99],
            &[30, 1, 1, 4, 2, 5, 6, 0, 99],
        );
    }
}
