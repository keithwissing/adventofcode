defmodule Day02 do
  import Adventofcode

  @moduledoc """
  Documentation for Day02.
  """

  @doc """
  iex> Day02.checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
  18
  """
  def checksum(sheet) do
    mm = Enum.map(sheet, &Enum.min_max/1)
    Enum.sum(Enum.map(mm, fn {n, x} -> x - n end))
  end

  def checksum2(sheet) do
    # Enum.sum(Enum.map(Enum.map(sheet, &Enum.min_max/1), fn ({n, x}) -> x - n end))
    sheet |> Enum.map(&Enum.min_max/1) |> Enum.map(fn {n, x} -> x - n end) |> Enum.sum()
  end

  @doc """
  iex> Day02.find_divisible(2, [5, 9, 2, 8])
  4
  iex> Day02.find_divisible(9, [5, 9, 2, 8])
  0
  iex> Day02.find_divisible(3, [9, 4, 7, 3])
  3
  """
  def find_divisible(first, row) do
    Enum.reduce(row, -1, fn x, acc ->
      if(rem(x, first) == 0, do: acc + div(x, first), else: acc)
    end)
  end

  def find_divisible(row) do
    Enum.reduce(row, 0, fn x, acc -> acc + find_divisible(x, row) end)
  end

  @doc """
  iex> Day02.part2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
  9
  """
  def part2(sheet) do
    Enum.map(sheet, &find_divisible/1) |> Enum.sum()
  end

  @doc """
  iex> Day02.part22([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
  9
  """
  def part22(sheet) do
    sheet
    |> Enum.map(fn row ->
      Enum.reduce(row, 0, fn first, acc ->
        acc +
          Enum.reduce(row, -1, fn x, acc ->
            if(rem(x, first) == 0, do: acc + div(x, first), else: acc)
          end)
      end)
    end)
    |> Enum.sum()
  end

  @doc """
  iex> Day02.part23([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
  9
  """
  def part23(sheet) do
    for row <- sheet,
        t1 <- row,
        t2 <- row,
        rem(t1, t2) == 0,
        div(t1, t2) > 1 do
      div(t1, t2)
    end
    |> Enum.sum()
  end

  def lines_to_sheet(lines) do
    a = Enum.map(lines, &String.split/1)
    Enum.map(a, fn r -> Enum.map(r, &String.to_integer/1) end)
  end

  def run do
    input = read_input(2)
    sheet = lines_to_sheet(input)
    answer(1, 39126, checksum(sheet))
    answer(1, 39126, checksum2(sheet))
    answer(2, 258, part2(sheet))
    answer(2, 258, part22(sheet))
    answer(2, 258, part23(sheet))
  end
end
