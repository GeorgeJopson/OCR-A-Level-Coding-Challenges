import React from "react";

function ToDoItem(props) {
  return (
    <div
      onClick={() => {
        props.onChecked(props.id);
      }}
    >
      <li>
        {props.title} ({props.date})
      </li>
    </div>
  );
}

export default ToDoItem;
