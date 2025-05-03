import React from 'react';

const FormInput = ({
  id,
  label,
  type = 'text',
  error = '',
  className = '',
  required = false,
  ...props
}) => {
  return (
    <div className="mb-4">
      {label && (
        <label 
          htmlFor={id} 
          className="block text-sm font-medium text-gray-700 mb-1"
        >
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </label>
      )}
      <input
        id={id}
        type={type}
        className={`
          w-full px-3 py-2 bg-white border ${error ? 'border-red-500' : 'border-gray-300'} 
          rounded-md shadow-sm placeholder-gray-400
          focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm
          ${className}
        `}
        aria-invalid={error ? 'true' : 'false'}
        aria-describedby={error ? `${id}-error` : undefined}
        {...props}
      />
      {error && (
        <p id={`${id}-error`} className="mt-1 text-sm text-red-600">
          {error}
        </p>
      )}
    </div>
  );
};

export default FormInput; 