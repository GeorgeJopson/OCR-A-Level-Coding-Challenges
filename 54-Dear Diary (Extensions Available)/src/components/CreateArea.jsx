import React, { useState } from "react";
import AddIcon from "@material-ui/icons/Add";
import Fab from "@material-ui/core/Fab";
import Zoom from "@material-ui/core/Zoom";

function CreateArea(props) {
  const [isExpanded, setExpanded] = useState(false);
  let date = new Date();
  let time = date.getDate() + "/" + date.getMonth() + "/" + date.getFullYear();
  const [note, setNote] = useState({
    title: "",
    content: "",
    date: time
  });

  function handleChange(event) {
    const { name, value } = event.target;

    setNote((prevNote) => {
      return {
        ...prevNote,
        [name]: value
      };
    });
  }

  function submitNote(event) {
    props.onAdd(note);
    setNote({
      title: "",
      content: "",
      date: time
    });
    event.preventDefault();
  }

  function expand() {
    setExpanded(true);
  }

  return (
    <div>
      <form className="create-note">
        <input
          name="title"
          onChange={handleChange}
          onClick={expand}
          value={note.title}
          placeholder={isExpanded ? "Title" : "Dear Diary.."}
          autoComplete="off"
        />

        {isExpanded && (
          <div>
            <textarea
              name="content"
              onChange={handleChange}
              value={note.content}
              placeholder="Add diary entry..."
              rows={isExpanded ? 3 : 1}
            />
            <p className="date">{note.date}</p>
          </div>
        )}
        <Zoom in={isExpanded}>
          <Fab onClick={submitNote}>
            <AddIcon />
          </Fab>
        </Zoom>
      </form>
    </div>
  );
}

export default CreateArea;
