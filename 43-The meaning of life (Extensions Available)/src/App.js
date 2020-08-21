import React, { useState } from "react";
import Cell from "./Cell";

export default function App() {
  const [cellState, setState] = useState([
    0,
    0,
    0,
    0,
    0,

    0,
    0,
    1,
    0,
    0,

    1,
    0,
    1,
    0,
    0,

    0,
    1,
    1,
    0,
    0,

    0,
    0,
    0,
    0,
    0,
    0
  ]);
  function changeState() {
    setState((prevState) =>
      prevState.map(function (cell, index) {
        let neighbours = [];
        //Top
        neighbours.push(prevState[index - 6]);
        neighbours.push(prevState[index - 5]);
        neighbours.push(prevState[index - 4]);
        if (index <= 4) {
          neighbours[0] = 0;
          neighbours[1] = 0;
          neighbours[2] = 0;
        }
        if (index % 5 === 0) {
          neighbours[0] = 0;
        } else if (index % 5 === 4) {
          neighbours[2] = 0;
        }
        //Sides
        neighbours.push(prevState[index - 1]);
        neighbours.push(prevState[index + 1]);
        if (index % 5 === 0) {
          neighbours[3] = 0;
        } else if (index % 5 === 4) {
          neighbours[4] = 0;
        }
        //Bottom
        neighbours.push(prevState[index + 4]);
        neighbours.push(prevState[index + 5]);
        neighbours.push(prevState[index + 6]);

        if (index >= 20) {
          neighbours[5] = 0;
          neighbours[6] = 0;
          neighbours[7] = 0;
        }
        if (index % 5 === 0) {
          neighbours[5] = 0;
        } else if (index % 5 === 4) {
          neighbours[7] = 0;
        }
        let aliveNeighbours = neighbours.reduce(
          (total, currentValue) => total + currentValue,
          0
        );
        if (prevState[index] === 1) {
          if (aliveNeighbours === 2 || aliveNeighbours === 3) {
            return 1;
          } else {
            return 0;
          }
        } else {
          if (aliveNeighbours === 3) {
            return 1;
          } else {
            return 0;
          }
        }
      })
    );
  }
  return (
    <div className="App">
      <Cell state={cellState[0]} cell={0} />
      <Cell state={cellState[1]} cell={1} />
      <Cell state={cellState[2]} cell={2} />
      <Cell state={cellState[3]} cell={3} />
      <Cell state={cellState[4]} cell={4} />
      <Cell state={cellState[5]} cell={5} />
      <Cell state={cellState[6]} cell={6} />
      <Cell state={cellState[7]} cell={7} />
      <Cell state={cellState[8]} cell={8} />
      <Cell state={cellState[9]} cell={9} />
      <Cell state={cellState[10]} cell={10} />
      <Cell state={cellState[11]} cell={11} />
      <Cell state={cellState[12]} cell={12} />
      <Cell state={cellState[13]} cell={13} />
      <Cell state={cellState[14]} cell={14} />
      <Cell state={cellState[15]} cell={15} />
      <Cell state={cellState[16]} cell={16} />
      <Cell state={cellState[17]} cell={17} />
      <Cell state={cellState[18]} cell={18} />
      <Cell state={cellState[19]} cell={19} />
      <Cell state={cellState[20]} cell={20} />
      <Cell state={cellState[21]} cell={21} />
      <Cell state={cellState[22]} cell={22} />
      <Cell state={cellState[23]} cell={23} />
      <Cell state={cellState[24]} cell={24} />
      <button onClick={changeState}>Click Me</button>
    </div>
  );
}
