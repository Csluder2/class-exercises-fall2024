import React, { useState } from "react";
import { Form, Input, Button, InputNumber, Carousel } from "antd";

export default function App() {
    const [tracks, setTracks] = useState([]);
    const [formValues, setFormValues] = useState({ searchTerm: "", limit: 5 });

    const carouselStyles = {
        width: "640px",
        border: "solid 1px #000",
        margin: "auto",
    };

    async function fetchData(values) {
        const { searchTerm, limit } = values;
        const baseURL = "https://www.apitutor.org/spotify/simple/v1/search";
        const url = `${baseURL}?q=${encodeURIComponent(searchTerm)}&type=track&limit=${limit}`;
        try {
            const response = await fetch(url);
            const data = await response.json();
            console.log(data);
            setTracks(data);
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    }

    function trackToIframe(track) {
        return (
            <iframe
                key={track.id}
                src={`https://open.spotify.com/embed/track/${track.id}?utm_source=generator`}
                width="100%"
                height="352"
                frameBorder="0"
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"
            ></iframe>
        );
    }

    return (
        <div style={{ width: "640px", margin: "auto", padding: "20px" }}>
            <Form
                layout="vertical"
                onFinish={(values) => {
                    setFormValues(values);
                    fetchData(values);
                }}
                style={{
                    border: "1px solid #ccc",
                    padding: "20px",
                    borderRadius: "10px",
                    backgroundColor: "#f9f9f9",
                }}
            >
                <Form.Item
                    label="Search Term"
                    name="searchTerm"
                    rules={[{ required: true, message: "Please enter a search term" }]}
                >
                    <Input placeholder="Enter an artist or song name" />
                </Form.Item>
                <Form.Item
                    label="Number of Songs"
                    name="limit"
                    rules={[
                        { required: true, type: "number", min: 1, max: 20, message: "Enter a number between 1 and 20" },
                    ]}
                >
                    <InputNumber min={1} max={20} />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Search
                    </Button>
                </Form.Item>
            </Form>

            {tracks.length > 0 ? (
                <div style={{ marginTop: "20px" }}>
                    <Carousel dotPosition="bottom" style={carouselStyles}>
                        {tracks.map(trackToIframe)}
                    </Carousel>
                </div>
            ) : (
                <p>Please search for songs to display them here.</p>
            )}
        </div>
    );
}


    


