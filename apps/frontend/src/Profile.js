// src/Profile.js
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Profile() {
  const [profile, setProfile] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        navigate('/login');
        return;
      }

      try {
        const res = await axios.get('/profile/me', {
             headers: { Authorization: token }   // your backend expects the raw token
              });
        setProfile(res.data);
      } catch (err) {
        // Unauthorized or error: drop token and send back to login
        localStorage.removeItem('token');
        navigate('/login');
      }
    };

    fetchProfile();
  }, [navigate]);

  if (!profile) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: 600, margin: 'auto', padding: 20 }}>
      <h2>Welcome, {profile.username}</h2>
      <p><strong>Email:</strong> {profile.email}</p>
      <p><strong>Role:</strong>  {profile.role}</p>
      <p><strong>Bio:</strong>   {profile.bio}</p>
      <button onClick={() => {
        localStorage.removeItem('token');
        navigate('/login');
      }}>Log Out</button>
    </div>
  );
}
