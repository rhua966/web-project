import React, { useState, useEffect } from 'react'
import ProductList from './ProductList'

export default function ProductPage() {

    const [products, setProducts] = useState([])

    useEffect(() => {
        fetch("/api/items").then(res => {
            if (!res.ok) {
                throw Error("ERROR Fetching Products!!!")
            }
            return res.json()
        }).then(data => {
            setProducts(data)
        })
    }, [])

    return (
        <div><ProductList products={products} /></div>
    )
    
}