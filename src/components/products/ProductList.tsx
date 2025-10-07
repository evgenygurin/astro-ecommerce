
import React from 'react';
import { useApiQuery } from '../../../hooks/interaction/useApiQuery';
import CardProduct from './cardProduct';

export default function ProductList() {
  const { data: products, isLoading, isError } = useApiQuery({ path: '/products' });

  if (isLoading) {
    return <div>Loading products...</div>;
  }

  if (isError) {
    return <div>Error loading products. Please make sure the backend server is running.</div>;
  }

  return (
    <div className="row mt-5">
      {products && products.map(product => (
        <div className="col-md-6 col-lg-3" key={product.id}>
          <CardProduct
            thumb_src={product.thumb_src}
            thumb_alt={product.thumb_alt}
            color={product.color}
            colors={product.colors}
            title={product.title}
            description={product.description}
            price={product.price}
            position="center"
          />
        </div>
      ))}
    </div>
  );
}
