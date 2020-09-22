import React, { useState, useEffect, useRef } from "react";
import { Button, InputGroup, FormControl} from "react-bootstrap";

export default function CommentsPage() {

    const [commentsData, setCommentsData] = useState([])
    const ref = useRef(null)

    
    useEffect(() => {

        fetchComment()

    }, [])

    const fetchComment = () => {
        fetch("/api/comment").then(res => {
            if (!res.ok) {
                throw Error("ERROR")
            }
            return res.json()
        }).then(data => {
            setCommentsData(data)
        }) 
    }

    // console.log(comments)
    const submitComment = (e) => {
        
        e.preventDefault() // Stop auto reloading behavior after submit form

        fetch("/api/comment", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "Name": ref.current['name'].value,
                "Comment": ref.current['comment'].value
            })
        }).then(res => {
            if (!res.ok) {
                throw Error("ERROR")
            }
            return res.json()
        }).then(data => {
            console.log(data)
            fetchComment()
        })
    }

    return (
        <div className='Comments'>
            <form className='CommentsInputArea' ref={ref} onSubmit={submitComment}>
                
                <InputGroup>
                    <InputGroup.Prepend>
                        {/* <InputGroup.Text></InputGroup.Text> */}
                    </InputGroup.Prepend>
                    <FormControl
                        as="textarea"
                        name="comment"
                        placeholder="Your Comment..."
                        aria-label="Your Comment..."
                    />
                </InputGroup>

                <InputGroup className="mb-3">
                    <FormControl
                        type="name"
                        name="name"
                        placeholder="Your name..."
                        aria-label="Your name..."
                        aria-describedby="basic-addon2"
                    />
                    <InputGroup.Append>
                        <Button variant="outline-secondary" type="submit">Button</Button>
                    </InputGroup.Append>
                </InputGroup>
            </form>

            <div className='CommentsData'>
                {commentsData.map(comment => {
                    return <p><em>{comment.Comment}</em> - <b>{comment.Name}</b></p>
                })}
            </div>
        </div>
    )
}