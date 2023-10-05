import './App.css';
import Navbar from './Navbar.js'
import DragAndDrop from './DragAndDrop.js'

function App() {
  const items = ['Item 1', 'Item 2', 'Item 3'];

  return (
    <div className='App'>
      <Navbar />

      <div className="square border border-3 border-secondary" style={{margin: '30px 150px', borderColor: 'blue' , borderWidth: 2, height:300, padding:"40px"}}>
        <DragAndDrop items={items} />
      </div>
      
    </div>
  );
}

export default App;
