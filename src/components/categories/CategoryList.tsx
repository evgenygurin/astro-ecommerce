
import React from 'react';
import { useApiQuery } from '../../../hooks/interaction/useApiQuery';
import CardCategory from '../products/cardCategory';

export default function CategoryList() {
  const { data: categories, isLoading, isError } = useApiQuery({ path: '/categories' });

  if (isLoading) {
    return <div>Loading categories...</div>;
  }

  if (isError) {
    return <div>Error loading categories. Please make sure the backend server is running.</div>;
  }

  return (
    <div className="row mb-8">
      <div className="d-block text-center mb-5">
        <h3>Shop by category</h3>
        <a className="text-dark font-weight-bold" href="#">Browse all categories &#62;</a>
      </div>
      {categories && categories.slice(0, 4).map(category => (
        <div className="col-md-6 col-lg-3" key={category.id}>
          <CardCategory
            thumb_src={category.thumb_src}
            title={category.title}
            collection={category.collection}
          />
        </div>
      ))}
    </div>
  );
}
