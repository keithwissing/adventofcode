defmodule Day02 do
    import Adventofcode
    @moduledoc """
    Documentation for Day02.
    """
  
    @doc """
    """
    def checksum(sheet) do
        mm = Enum.map(sheet, &Enum.min_max/1)
        Enum.sum(Enum.map(mm, fn ({n, x}) -> x - n end))
    end

    def checksum2(sheet) do
        #Enum.sum(Enum.map(Enum.map(sheet, &Enum.min_max/1), fn ({n, x}) -> x - n end))
        sheet |> Enum.map(&Enum.min_max/1) |> Enum.map(fn({n, x}) -> x - n end) |> Enum.sum
        #Enum.sum(Enum.map(Enum.map(sheet, &Enum.min_max/1), fn ({n, x}) -> x - n end))
    end

    def lines_to_sheet(lines) do
        a = Enum.map(lines, &String.split/1)
        Enum.map(a, fn(r) -> Enum.map(r, &String.to_integer/1) end)
    end

    def run do
        input = read_input(2)
        sheet = lines_to_sheet(input)
        answer(1, 39126, checksum sheet)
        answer(1, 39126, checksum2 sheet)
        #answer(2, 258, captcha2 input)
    end

  end
  