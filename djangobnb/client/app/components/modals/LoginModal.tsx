'use client';

import React from 'react';
import Modal from "./Modal";
import useLoginModal from '../hooks/useLoginModal';
import CustomButton from '../forms/CustomButton';

const LoginModal = () => {
  const loginModal = useLoginModal();
  const content = (
    <>
      <h2 className="mb-6 text-2xl">Welcome to Djangobnb, please login to continue</h2>
      <form className="space-y-4">
        <input 
          placeholder="Your e-mail address"
          type="email"
          className="w-full h-[54px] border px-4 border-gray-300 rounded-xl"
        />
        <input 
          placeholder="Your password"
          type="password"
          className="w-full h-[54px] border px-4 border-gray-300 rounded-xl"
        />
        <div className="p-5 bg-airbnb text-white rounded-xl opacity-80">
          The error message
        </div>
        <CustomButton 
          label="Submit"
          onClick={() => console.log('Test')}
        />
      </form>
    </>
  )
  return (
    <Modal 
      isOpen={loginModal.isOpen}
      close={loginModal.close}
      label="Log in"
      content={content}
    />
  )
}

export default LoginModal;
