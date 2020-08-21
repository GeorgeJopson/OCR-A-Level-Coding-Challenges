import React from "react";

function Cell(props) {
  let cellNum = props.cell;
  let column = cellNum % 5;
  let row = Math.floor(cellNum / 5);
  let position = {
    left: column * 110,
    top: row * 110
  };
  return (
    <div
      style={position}
      className={props.state === 1 ? "cell on" : "cell off"}
    ></div>
  );
}

export default Cell;
