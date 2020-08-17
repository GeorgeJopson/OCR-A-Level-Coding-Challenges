import React, { useState } from "react";

function InputArea(props) {
  const [event, setEvent] = useState({
    title: "",
    date: ""
  });

  function handleChange(event) {
    const { name, value } = event.target;
    setEvent((prevValue) => {
      return {
        ...prevValue,
        [name]: value
      };
    });
  }
  return (
    <div className="form">
      <input
        onChange={handleChange}
        name="title"
        type="text"
        value={event.title}
        placeholder="Title"
        autoComplete="off"
      />
      <input
        onChange={handleChange}
        name="date"
        type="date"
        placeholder="Date"
        value={event.date}
      />
      <button
        onClick={() => {
          setEvent({ title: "", date: "" });
          props.addEvent(event.title, event.date);
        }}
      >
        <span>Add</span>
      </button>
    </div>
  );
}

export default InputArea;
