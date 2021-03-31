Rails.application.routes.draw do
  
  root 'posts#index'

  get 'about' => 'pages#about'

  resources :posts
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
