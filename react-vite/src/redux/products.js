// -------------------------------
// PRODUCTS REDUX SLICE
// Dream Grid Interactive Studios
// -------------------------------

const GET_PRODUCTS = "products/GET_PRODUCTS";
const GET_ONE = "products/GET_ONE";


// -------------------------------
// ACTION CREATORS
// -------------------------------
const getProducts = (products) => ({
  type: GET_PRODUCTS,
  products,
});

const getOneProduct = (product) => ({
  type: GET_ONE,
  product,
});


// -------------------------------
// THUNKS
// -------------------------------

// Get EVERY product (flat list)
export const fetchAllProducts = () => async (dispatch) => {
  const res = await fetch("/api/products/");
  if (res.ok) {
    const data = await res.json();
    dispatch(getProducts(data));
  }
};

// Get a single product by SKU
export const fetchProductBySku = (sku) => async (dispatch) => {
  const res = await fetch(`/api/products/sku/${sku}`);
  if (res.ok) {
    const data = await res.json();
    dispatch(getOneProduct(data));
  }
};


// -------------------------------
// INITIAL STATE
// -------------------------------
const initialState = {
  all: [],      // flat list of EVERYTHING
  single: null, // optional: one product
};


// -------------------------------
// REDUCER
// -------------------------------
export default function productsReducer(state = initialState, action) {
  switch (action.type) {

    case GET_PRODUCTS:
      return {
        ...state,
        all: action.products,
      };

    case GET_ONE:
      return {
        ...state,
        single: action.product,
      };

    default:
      return state;
  }
}
