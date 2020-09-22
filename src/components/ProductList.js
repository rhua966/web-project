import React from 'react'
import Product from './Product'

export default function ProductList({ products}) {

    // const [products, setProducts] = useState([])

    // useEffect(() => {
    //     fetch("/api/items").then(res => {
    //         if (!res.ok) {
    //             throw Error("ERROR Fetching Products!!!")
    //         }
    //         return res.json()
    //     }).then(data => {
    //         setProducts(data)
    //     })
    // }, [])

    console.log(products);
    // return null
    // return <div>{products}</div>
    return <div>{products.map(product => { return <Product product={product}/>})}</div>
}