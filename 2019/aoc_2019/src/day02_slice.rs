fn step(memory: &mut [i32], ip: usize) -> bool {
    let instr = memory[ip as usize];
    if instr == 99 {
        return false;
    }
    let p1 = memory[(ip + 1)] as usize;
    let p2 = memory[(ip + 2)] as usize;
    let p3 = memory[(ip + 3)] as usize;
    if instr == 1 {
        memory[p3] = memory[p1] + memory[p2];
    }
    if instr == 2 {
        memory[p3] = memory[p1] * memory[p2];
    }
    true
}

fn run(memory: &mut [i32]) -> i32 {
    let mut ip: usize = 0;
    let mut con = step(memory, ip);
    while con {
        ip += 4;
        con = step(memory, ip);
    }
    memory[0]
}

fn run_nv(program: &[i32], noun: i32, verb: i32) -> i32 {
    let mut memory = program.to_vec();
    memory[1] = noun;
    memory[2] = verb;
    run(&mut memory)
}

fn part2(program: &[i32]) -> i32 {
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
    let p1 = run_nv(&program, 12, 2);
    let p2 = part2(&program);
    (p1, p2)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn test_run(program: &[i32], expected: &[i32]) {
        let mut memory = program.to_vec();
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
