import React, {useCallback} from 'react'
import {useDropzone} from 'react-dropzone'

function DragAndDrop() {
  const onDrop = useCallback(acceptedFiles => {
    console.log(acceptedFiles)
  }, [])
  const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop})

  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />
      {
        isDragActive ?
          <p>Drop the files here ...</p> :
          <div>
            <p style={{fontSize:70, fontWeight: 'bold', color: '#888888', paddingBottom:"20px"}}>Drag and drop..</p>
            <button type="button" class="btn btn-outline-secondary">Select File</button>
          </div>
      }
    </div>
  )
}

export default DragAndDrop;