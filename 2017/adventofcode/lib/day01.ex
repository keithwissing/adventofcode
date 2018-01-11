defmodule Day01 do
    import Adventofcode
    @moduledoc """
    Documentation for Day01.
    """
  
    @doc """
    iex> Day01.captcha1("1122")
    3
    iex> Day01.captcha1("1111")
    4
    iex> Day01.captcha1("1234")
    0
    iex> Day01.captcha1("91212129")
    9
    """
    def captcha1(digits) do
        l = String.graphemes(digits)
        [h|t] = l
        l2 = t ++ [h]
        z = Enum.zip(l, l2)
        Enum.reduce z, 0, fn(v, a) ->
            case v do
                {x, x} -> a + String.to_integer(x)
                {_, _} -> a
            end
        end
    end

    @doc """
    iex> Day01.captcha2("1212")
    6
    iex> Day01.captcha2("1221")
    0
    iex> Day01.captcha2("123425")
    4
    iex> Day01.captcha2("123123")
    12
    iex> Day01.captcha2("12131415")
    4
    """
    def captcha2(digits) do
        l = String.graphemes(digits)
        len = length(l)/2 |> round
        [a, b] = Enum.chunk(l, len)
        l2 = b ++ a
        z = Enum.zip(l, l2)
        Enum.reduce z, 0, fn(v, a) ->
            case v do
                {x, x} -> a + String.to_integer(x)
                {_, _} -> a
            end
        end
    end

    def run do
        input = read_input(1)
        answer(1, 1144, captcha1 input)
        answer(2, 1194, captcha2 input)
    end

  end
  