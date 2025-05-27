import React from 'react'
import PropertyListItem from './PropertyListItem'

const PropertyList = () => {
  return (
    <div className="max-w-[1500px] mx-auto px-6">
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6 h-full">
        <PropertyListItem />
        <PropertyListItem />
        <PropertyListItem />
        <PropertyListItem />
      </div>
    </div>
  )
}

export default PropertyList
