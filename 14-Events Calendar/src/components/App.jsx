import React, { useState } from "react";
import ToDoItem from "./ToDoItem";
import InputArea from "./InputArea";

function App() {
  const [events, setEvents] = useState([]);

  function addEvent(inputTitle, inputDate) {
    let dateClash = false;
    events.forEach((event) => {
      if (event.date === inputDate) {
        dateClash = true;
        alert("There is a date clash with the event: " + event.title);
      }
    });

    if (!dateClash) {
      setEvents((prevEvents) => {
        return [...prevEvents, { title: inputTitle, date: inputDate }];
      });
    }
  }

  function deleteEvent(id) {
    setEvents((prevEvents) => {
      return prevEvents.filter((event, index) => {
        return index !== id;
      });
    });
  }

  return (
    <div className="container">
      <div className="heading">
        <h1>Calendar</h1>
      </div>
      <InputArea addEvent={addEvent} />
      <div>
        <ul>
          {events.map((event, index) => (
            <ToDoItem
              key={index}
              id={index}
              title={event.title}
              date={event.date}
              onChecked={deleteEvent}
            />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
