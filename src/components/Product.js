import React from 'react'
import {
    Card, CardImg, CardText, CardBody,
    CardTitle, CardSubtitle, Button
} from 'reactstrap';
import "../App.css"

export default function Product({ product }) {

    return (
        <div className="card-grid">
            <Card>
                <CardImg top width="50px" src={"/api/itemimg?id=" + product.Id} alt="Card image cap" />
                <CardBody>
                    <CardTitle>{product.Title}</CardTitle>
                    <CardSubtitle>{product.Type} from {product.Origin}</CardSubtitle>
                    <CardText>${product.Price}</CardText>
                    <Button>Buy</Button>
                </CardBody>
            </Card>
        </div>
    )
}