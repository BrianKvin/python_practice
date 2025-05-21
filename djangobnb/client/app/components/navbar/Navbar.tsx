import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import Search from './Search'
import UserNav from './UserNav'
import AddPropertyButton from './AddPropertyButton'

const Navbar = () => {
  return (
    <nav className="w-full fixed top-0 left-0 bg-white border-b z-10 py-6">
      <div className="max-w-[1500px] mx-auto px-6">
        <div className="flex justify-between items-center">
          <Link href="/">
            <Image
              width={120}
              height={50}
              src="/logo.png"
              alt="bnb logo"
            />
          </Link>
          <div className="flex space-x-6">
            <Search />
          </div>
          <div className="flex items-center space-x-6"> 
            <AddPropertyButton />
            <UserNav />
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
